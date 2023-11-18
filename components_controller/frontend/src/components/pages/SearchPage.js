import React from "react";
import { useLocation } from "react-router-dom";

const SearchPage = () => {
	const { state } = useLocation();

	// Check if state contains the matchingGame object
	const matchingGame = state && state.matchingGame ? state.matchingGame : null;

	// Use matchingGame as needed in your component

	return (
		<div style={{ color: "white" }}>
			<h2>Search Game Page</h2>
			{matchingGame ? (
				<div>
					{/* Display details of matchingGame */}
					<p>Name: {matchingGame.info.name}</p>
					{/* Add other details here */}
				</div>
			) : (
				<p>No matching game found.</p>
			)}
			<h1>TO BE OR NOT IMPEMENTED</h1>
		</div>
	);
};

export default SearchPage;
