import React from "react";
import GameSearch from "../GameSearch";
const Circle = () => {
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
