import React, { Component } from "react";
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Routes,
	Link,
	Redirect,
} from "react-router-dom";
import PopularGamesPage from "./PopularGamesPage";
import Home from "./Pages/Home";
import SearchPage from "./Pages/SearchPage";
import GameSearch from "./GameSearch";

export default class Pages extends Component {
	/**
     * Componenta care definește traseul paginilor în aplicație utilizând React Router.
     * Această componentă conține rute pentru paginile principale ale aplicației.
     */
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<Router>
				{/* Definirea sistemului de rute pentru diferitele pagini */}
				<Routes>
					{/* Ruta pentru pagina principală a aplicației */}
					<Route path="/" element={<Home />} />

					{/* Ruta pentru pagina de jocuri populare */}
					<Route path="/popular-games" element={<PopularGamesPage />} />

					{/* Ruta pentru pagina de căutare a jocurilor */}
					<Route path="/search-game/:query" element={<SearchPage />} />
				</Routes>
			</Router>
		);
	}
}
