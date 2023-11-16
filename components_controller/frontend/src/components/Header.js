import React from "react";
import Button from "./smallComponents/Button";
import { FaHatWizard } from "react-icons/fa";
import { FaComputer } from "react-icons/fa6";

const Header = () => {
	const myArray = ["thing 1", "thing 2", "thing 3"];
	const handleClick = (item) => {
		console.log("Div clicked!" + item);
	};
	return (
		<div className="header-wrapper">
			<div className="header">
				<div
					style={{
						paddingLeft: "15%",
						paddingTop: "20px",
						paddingBottom: "20px",
					}}
				>
					<div className="logo">
						<FaHatWizard size={35} color="white" />
						<div style={{ color: "white" }}>CanMyPcRunIt?</div>
					</div>
				</div>
				<div className="menu-list">
					{myArray.map((item, index) => (
						<Button
							key={index}
							className="type1"
							onClick={() => handleClick(item)}
						>
							{item}
						</Button>
					))}
				</div>
				<div></div>
			</div>
		</div>
	);
};

export default Header;
