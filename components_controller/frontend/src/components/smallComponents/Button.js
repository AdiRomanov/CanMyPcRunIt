import React from "react";

const Button = ({ keyProp = "1", onClick, className, children }) => {
	return (
		<div
			{...(keyProp && { key: keyProp })}
			onClick={onClick}
			className={className}
		>
			{children}
		</div>
	);
};

export default Button;
