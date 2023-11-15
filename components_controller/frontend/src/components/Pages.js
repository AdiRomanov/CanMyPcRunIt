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
export default class Pages extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/search-game" element={<SearchPage />} />
					<Route path="/popular-games" element={<PopularGamesPage />} />
				</Routes>
			</Router>
		);
	}
}
