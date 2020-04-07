import API_BASE from './URL'

async function getBrokerAccounts(){
	let response = await fetch(`${API_BASE}/broker_accounts`)
	let data = await response.json()
	return data
}


export default getBrokerAccounts;
