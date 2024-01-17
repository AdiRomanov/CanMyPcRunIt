import React, { Component } from "react";
import { render } from "react-dom";
import Pages from "./Pages";

export default class App extends Component {
		/**
     * Componenta principală a aplicației.
	 * Metoda render():
	 * - Returnează conținutul aplicației, inclusiv componenta 'Pagini'.
	 *
	 */
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

// Renderează aplicația în elementul HTML cu id-ul "aplicatie".
const appDiv = document.getElementById("app");
render(<App />, appDiv);
