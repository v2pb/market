import React, { createContext, useState, useEffect, useCallback, useMemo } from 'react';

interface GlobalContextType {
  globalStateMap: Map<string, any>;
  addGlobalStateData: (key: string, value: any) => void;
}

export const GlobalContext = createContext<GlobalContextType | undefined>(undefined);

export const GlobalProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [globalStateMap, setGlobalStateMap] = useState<Map<string, any>>(new Map());

  useEffect(() => {
    // Runs only once when app loads/refreshed
    const data = JSON.parse(localStorage.getItem("formdata") || "[]");
    const map = new Map<string, any>();
    data.forEach((obj: { [key: string]: any }) => {
      Object.entries(obj).forEach(([key, val]) => {
        map.set(key, val);
      });
    });
    setGlobalStateMap(map);
  }, []);

  const addGlobalStateData = useCallback((key: string, value: any) => {
    setGlobalStateMap(prev => {
      const newMap = new Map(prev);
      newMap.set(key, value);

      // Also update localStorage whenever state updates
      const objArray = Array.from(newMap.entries()).map(([k, v]) => ({ [k]: v }));
      localStorage.setItem("formdata", JSON.stringify(objArray));

      return newMap;
    });
  }, []);

  const value = useMemo(() => ({ globalStateMap, addGlobalStateData }), [globalStateMap, addGlobalStateData]);

  return (
    <GlobalContext.Provider value={value}>
      {children}
    </GlobalContext.Provider>
  );
};
