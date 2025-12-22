import figlet from "figlet";
import chalk from "chalk";


figlet("Evolve AI", (err, text) => {
  if (err) return console.error(err);
  console.log(chalk.magenta(text));
});





