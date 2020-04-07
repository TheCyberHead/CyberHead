import API_BASE from './URL'

async function portfolioStrategies(){
	let response = await fetch(`${API_BASE}/portfolio_strategies`)
	let data = await response.json()
	return data
}


export default portfolioStrategies;