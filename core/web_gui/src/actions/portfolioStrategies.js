async function portfolioStrategies(){
	let response = await fetch(`http://localhost:5000/portfolio_strategies`)
	let data = await response.json()
	return data
}


export default portfolioStrategies;