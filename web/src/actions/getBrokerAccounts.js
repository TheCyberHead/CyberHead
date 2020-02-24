async function getBrokerAccounts(){
	let response = await fetch(`http://localhost:5000/broker_accounts`)
	let data = await response.json()
	return data
}


export default getBrokerAccounts;