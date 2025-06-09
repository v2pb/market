"""
Kite Connect login handler module.
This module provides functionality to authenticate with the Kite Connect API.
"""

import logging
import json
import os
from datetime import datetime
from typing import Optional, Dict
from kiteconnect import KiteConnect
from config import CREDENTIALS
from container import Container

# Configure logging with a more detailed format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class KiteLoginError(Exception):
    """Custom exception for Kite login related errors."""
    pass

class KiteLogin:
    """Handles authentication with Kite Connect API."""
    
    def __init__(self, api_key: str, api_secret: str, request_token: Optional[str] = None):
        """
        Initialize KiteLogin instance.
        
        Args:
            api_key (str): The API key from Kite Connect
            api_secret (str): The API secret from Kite Connect
            request_token (Optional[str]): Request token from the login process
        """
        self._api_key = api_key
        self._api_secret = api_secret
        self._request_token = request_token
        self.kite = None
        self.access_token = None
        self._session_file = "kite_session.json"
        
    def _save_session(self, access_token: str) -> None:
        """Save access token and timestamp to file."""
        session_data = {
            "access_token": access_token,
            "timestamp": datetime.now().isoformat(),
            "api_key": self._api_key
        }
        try:
            with open(self._session_file, "w") as f:
                json.dump(session_data, f)
            logger.info("Session data saved successfully")
        except Exception as e:
            logger.error(f"Failed to save session: {e}")

    def _load_session(self) -> Optional[Dict]:
        """Load saved session if it exists."""
        try:
            if os.path.exists(self._session_file):
                with open(self._session_file, "r") as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load session: {e}")
        return None

    def login(self) -> KiteConnect:
        """
        Perform the login process with Kite Connect.
        Attempts to use saved session first, falls back to new login if needed.
        
        Returns:
            KiteConnect: Authenticated KiteConnect instance
        
        Raises:
            KiteLoginError: If login process fails
        """
        try:
            # Check if we already have a valid instance in the container
            existing_kite = Container.get_kite_instance()
            if existing_kite:
                try:
                    # Verify the existing instance
                    existing_kite.margins()
                    logger.info("Using existing Kite instance from container")
                    return existing_kite
                except Exception:
                    logger.warning("Existing Kite instance invalid, creating new one")
            
            logger.info("Initializing Kite Connect")
            self.kite = KiteConnect(api_key=self._api_key)
            
            # Try to load existing session
            session_data = self._load_session()
            if session_data and session_data.get("api_key") == self._api_key:
                try:
                    logger.info("Attempting to use saved session")
                    self.access_token = session_data["access_token"]
                    self.kite.set_access_token(self.access_token)
                    # Verify the token works by making a simple API call
                    self.kite.margins()
                    logger.info("Successfully restored previous session")
                    Container.set_kite_instance(self.kite)
                    return self.kite
                except Exception as e:
                    logger.warning(f"Saved session invalid, getting new session: {e}")
            
            # If we get here, we need a new session
            login_url = self.kite.login_url()
            logger.info(f"Please visit this URL to login: {login_url}")
            
            self._request_token = input("Enter the request token: ").strip()
            if not self._request_token:
                raise KiteLoginError("Request token cannot be empty")
            
            logger.info("Generating session with request token")
            data = self.kite.generate_session(
                request_token=self._request_token,
                api_secret=self._api_secret
            )
            
            self.access_token = data["access_token"]
            self.kite.set_access_token(self.access_token)
            
            # Save the new session
            self._save_session(self.access_token)
            
            # Store in container
            Container.set_kite_instance(self.kite)
            
            logger.info("Successfully logged in to Kite Connect")
            return self.kite
            
        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            raise KiteLoginError(f"Failed to login: {str(e)}")

def get_kite_instance() -> Optional[KiteConnect]:
    """Get a singleton KiteConnect instance."""
    # First check if we have an existing instance
    kite = Container.get_kite_instance()
    if kite:
        try:
            # Verify the instance is still valid
            kite.margins()
            return kite
        except Exception:
            logger.warning("Existing Kite instance expired")
    
    # Create new instance if needed
    try:
        kite_login = KiteLogin(
            api_key=CREDENTIALS["api_key"],
            api_secret=CREDENTIALS["api_secret"]
        )
        kite = kite_login.login()
        logger.info(f"Access token: {kite_login.access_token}")
        return kite
    
    except KiteLoginError as e:
        logger.error(f"Login failed: {e}")
        return None

if __name__ == "__main__":
    get_kite_instance()