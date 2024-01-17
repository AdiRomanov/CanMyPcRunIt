import React from "react";
import GameSearch from "../GameSearch";
const Circle = () => {
	/**
     * Componenta reprezentând un cerc stilizat cu o căutare de jocuri în interior.
     */
	return (
		<>
			<div className="circle-wrapper">
				<div className="circle">
					<span></span>
					<span></span>
					<span></span>
					<span></span>
				</div>
			</div>
			<div className="circle-wrapper search">
				<GameSearch />
			</div>
		</>
	);
};

export default Circle;
