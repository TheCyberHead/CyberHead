import API_BASE from './URL'

async function getStrategies(strategy){
	let response = await fetch(`${API_BASE}/get_strategies`)
	let data = await response.json()
	return data
}

async function getStrategy(strategy){
	let response = await fetch(`${API_BASE}/get_strategy/${strategy}`)
	let data = await response.json()
	return data
}

async function getStrategyEdit(name){
	let response = await fetch(`${API_BASE}/get_strategy_edit/${name}`)
	let data = await response.json()
	return data
}

async function loadStrategiesEditor(){
	let response = await fetch(`${API_BASE}/get_strategies_edit`)
	let data = await response.json()
	return data
}

export {
	getStrategies, 
	getStrategy, 
	getStrategyEdit, 
	loadStrategiesEditor
};