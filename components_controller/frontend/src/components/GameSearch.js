import React, { useState, useEffect } from "react";
import Button from "./smallComponents/Button";
import { Link, useNavigate } from "react-router-dom";
const GameSearch = () => {
	const [query, setQuery] = useState("");
	const [results, setResults] = useState([]);
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const [searched, setSearched] = useState(false);
	const [matchingGame, setMatchingGame] = useState(null);
	const navigate = useNavigate();

	// Function to handle the API response
	const handleApiResponse = async (response) => {
		try {
			if (!response.ok) {
				throw new Error("Failed to fetch search results");
			}

			const data = await response.json();
			console.log("API Response:", data);

			return data;
		} catch (error) {
			setError("An error occurred while fetching search results.");
			console.error("Error:", error);
			throw error; // Re-throw the error to stop further processing
		} finally {
			setLoading(false);
		}
	};

	// Function to process the data from the API
	const handleData = (data) => {
		// Find the matching game by info.name
		const matchingGame = data.find(
			(game) => game.info.name.toLowerCase() === query.toLowerCase()
		);
		setResults(data);
		setMatchingGame(matchingGame);
		if (matchingGame) {
			navigate(`/search-game/${query}`, { state: { matchingGame } });
		}
	};

	// Function to handle the search
	const handleSearch = async () => {
		setLoading(true);

		setError(null);
		setSearched(true);

		try {
			// Add a delay of 1.5 seconds before making the API request
			await new Promise((resolve) => setTimeout(resolve, 1500));

			// Perform a fetch or use your preferred method to send a request to the Django backend
			const response = await fetch(
				`http://127.0.0.1:8000/api/search-game/?q=${query}`
			);
			const data = await handleApiResponse(response);

			handleData(data);
		} catch (error) {
			// Error handling is already done in handleApiResponse
		}
	};

	return (
		<div className="home-page-search-wrapper">
			<h1
				style={{
					color: "white",
					textAlign: "center",
					fontFamily: "Arial",
					fontWeight: "bold",
				}}
			>
				Can my Pc run:
			</h1>
			<input
				type="text"
				value={query}
				onChange={(e) => setQuery(e.target.value)}
			/>

			<Button className="type2" onClick={() => handleSearch()}>
				Search
			</Button>

			{loading && <p style={{ color: "white" }}>Loading...</p>}

			{error && <p style={{ color: "red" }}>{error}</p>}

			{searched && (
				<div>
					{matchingGame ? (
						<>{console.log(matchingGame)}</>
					) : (
						<>
							{!loading ? (
								<p
									style={{
										color: "white",
										fontFamily: "Arial",
										marginTop: "40px",
									}}
								>
									No matching result found.
								</p>
							) : (
								<></>
							)}
						</>
					)}
				</div>
			)}
		</div>
	);
};

export default GameSearch;
