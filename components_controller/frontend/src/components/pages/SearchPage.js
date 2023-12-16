import React from "react";
import { useLocation } from "react-router-dom";

const SearchPage = () => {
	const { state } = useLocation();

	// Check if state contains the matchingGame object
	const matchingGame = state && state.matchingGame ? state.matchingGame : null;

	// Use matchingGame as needed in your component

	return (
	  <div>
		{matchingGame ? (
		  <p style={{ color: "white", fontFamily: "Arial", marginTop: "40px" }}>
			<p1>Name: {matchingGame.name}</p1><br />
			<p2>Description: {matchingGame.description}</p2><br />
			<p2>Developer: {matchingGame.developer}</p2><br />
			<p2>Minimum requirements for {matchingGame.name}:</p2><br />
			<p3>Ram: {matchingGame.ram_min}</p3><br />
			<p3>Cpu: {matchingGame.cpu_min}</p3><br />
			<p3>Gpu: {matchingGame.gpu_min}</p3><br />
			<p3>OS: {matchingGame.OS_min}</p3><br />
			<p3>Storage: {matchingGame.storage_min}</p3><br />
			<p2>Recommended requirements for {matchingGame.name}:</p2><br />
			<p3>Ram: {matchingGame.ram_rec}</p3><br />
			<p3>Cpu: {matchingGame.cpu_rec}</p3><br />
			<p3>Gpu: {matchingGame.gpu_rec}</p3><br />
			<p3>OS: {matchingGame.OS_rec}</p3><br />
			<p3>Storage: {matchingGame.storage_rec}</p3><br />
		  </p>
		) : (
		  <p style={{ color: "white", fontFamily: "Arial", marginTop: "40px" }}>
			No matching result found.
		  </p>
		)}
	  </div>
	);


};

export default SearchPage;
