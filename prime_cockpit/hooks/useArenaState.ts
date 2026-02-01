import { useEffect, useState } from "react";

export function useArenaState() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [state, setState] = useState<any>(null);

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

  return { loading, error, state };
}
