const path = require("path");
const webpack = require("webpack");

/**
 * Configurația Webpack pentru construcția și optimizarea proiectului frontend.
 *
 * @param {object} env - Variabilele de mediu transmise către configurație.
 * @param {object} argv - Argumente adiționale transmise către configurație.
 * @returns {object} - Configurația finală a Webpack.
 */
module.exports = (env, argv) => {
  return {
    entry: "./src/index.js",
    output: {
      path: path.resolve(__dirname, "./static/frontend"),
      filename: "[name].js",
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
          },
        },
      ],
    },
    optimization: {
      minimize: argv.mode === "production",
    },
    plugins: argv.mode === "production"
      ? [
          new webpack.DefinePlugin({
            "process.env.NODE_ENV": JSON.stringify("production"),
          }),
        ]
      : [],
  };
};
