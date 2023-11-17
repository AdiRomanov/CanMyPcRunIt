// src/components/GameSearch.js
import React, { useState } from 'react';

const GameSearch = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searched, setSearched] = useState(false);

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSearched(true);

    try {
      // Add a delay of 1.5 seconds before making the API request
      await new Promise(resolve => setTimeout(resolve, 1500));

      // Perform a fetch or use your preferred method to send a request to the Django backend
      const response = await fetch(`http://127.0.0.1:8000/api/search-game/?q=${query}`);
      if (!response.ok) {
        throw new Error('Failed to fetch search results');
      }

      const data = await response.json();
      console.log('API Response:', data);
      setResults(data.results);
    } catch (error) {
      setError('An error occurred while fetching search results.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1 style={{ color: 'white' }}>Game Search</h1>

      <form onSubmit={handleSearch}>
        <label style={{ color: 'white' }}>
          Search:
          <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
        </label>
        <button type="submit" disabled={loading} style={{ color: 'white', backgroundColor: 'blue' }}>
          Search
        </button>
      </form>

      {loading && <p style={{ color: 'white' }}>Loading...</p>}

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {searched && (
        <div>
          {results.length > 0 ? (
            <>
              <h2 style={{ color: 'white' }}>Search Results:</h2>
              <div style={{ color: 'white' }}>
                {/* Find the matching game by info.name */}
                const matchingGame = results.find((game) => game.info.name === query);

                {/* Display details for the matching game */}
                {matchingGame ? (
                  <>
                    <p>Name: {matchingGame.info.name}</p>
                    <p>Description: {matchingGame.info.description}</p>
                    <p>Developer: {matchingGame.info.developer}</p>
                    {/* Add other fields as needed */}
                  </>
                ) : (
                  <p style={{ color: 'white' }}>No matching result found.</p>
                )}
              </div>
            </>
          ) : (
            <p style={{ color: 'white' }}>No results found.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default GameSearch;
