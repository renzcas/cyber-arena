import { useEffect, useState } from "react";

export function useArenaState() {
  const [state, setState] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/api/arena/state")
      .then(r => r.json())
      .then(data => {
        setState(data);
        setLoading(false);
      })
      .catch(e => {
        setError(e.message);
        setLoading(false);
        
      });
  }, []);

  return { state, loading, error };
}
