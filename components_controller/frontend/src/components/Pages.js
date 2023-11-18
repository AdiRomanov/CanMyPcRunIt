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
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/popular-games" element={<PopularGamesPage />} />
					<Route path="/search-game/:query" element={<SearchPage />} />
				</Routes>
			</Router>
		);
	}
}
