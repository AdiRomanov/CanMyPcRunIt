import React, { useState, useEffect } from "react";
import Button from "./smallComponents/Button";
import { Link, useNavigate } from "react-router-dom";
const GameSearch = () => {
	/**
     * Componenta care gestionează căutarea jocurilor pe pagina principală.
     * Folosește un câmp de intrare, un buton de căutare și afișează rezultatele.
     */
	const [query, setQuery] = useState("");
	const [results, setResults] = useState([]);
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState(null);
	const [searched, setSearched] = useState(false);
	const [matchingGame, setMatchingGame] = useState(null);
	const navigate = useNavigate();


	// Funcție pentru a gestiona răspunsul API-ului
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
			throw error; // Aruncă din nou eroarea pentru a opri procesarea ulterioară
		} finally {
			setLoading(false);
		}
	};

	// Funcție pentru a procesa datele de la API
	const handleData = (data) => {
		// Găsește jocul potrivit după info.name
		const matchingGame = data.find(
			(game) => game.name.toLowerCase() === query.toLowerCase()
		);
		setResults(data);
		setMatchingGame(matchingGame);
		if (matchingGame) {
			navigate(`/search-game/${query}`, { state: { matchingGame } });
		}
	};

	// Funcție pentru a gestiona căutarea
	const handleSearch = async () => {
		setLoading(true);

		setError(null);
		setSearched(true);

		try {
			// Adaugă un întârziere de 1.5 secunde înainte de a face cererea API
            // await new Promise((rezolva) => setTimeout(rezolva, 1500));

            // Realizează o cerere fetch sau folosește metoda preferată pentru a trimite o cerere către backend-ul Django
			const response = await fetch(
				`http://127.0.0.1:8000/api/search-game/?q=${query}`
					//'http://127.0.0.1:8000/api/search-game-by-name/?q=${query}'
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
