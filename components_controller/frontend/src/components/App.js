import React, { Component } from "react";
import { render } from "react-dom";
import Pages from "./Pages";

export default class App extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div>
				<Pages />
			</div>
		);
	}
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
