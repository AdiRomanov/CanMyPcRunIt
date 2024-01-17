import React from "react";

const Button = ({ keyProp = "1", onClick, className, children }) => {
		    /**
     * Componenta reprezentând un buton simplu.
     *
     * Proprietăți:
     * - keyProp: Cheia unică a elementului (implicit '1').
     * - onClick: Funcția apelată la clic pe buton.
     * - className: Clasele CSS aplicate butonului.
     * - children: Conținutul butonului (text sau alte componente).
     */
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
