import React, { Component} from "react";
import {BrowserRouter as Router,
        Switch,
        Route,
        Routes,
        Link,
        Redirect} from "react-router-dom";
import SearchGamesPage from "./SearchGamePage";
import PopularGamesPage from "./PopularGamesPage";
export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route path="/" element={<p>This is the home page</p> } />
                    <Route path="/search-game" element={<SearchGamesPage />} />
                    <Route path='/popular-games' element={<PopularGamesPage />} />
                </Routes>
            </Router>
        );
    }
}