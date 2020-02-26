async function createDataSet(dataset){
	let response = await fetch(`http://localhost:5000/datasets`,{
			method: 'POST',
			body: JSON.stringify(dataset),
			headers:{
				'Content-Type': 'application/json'
			}
		})
	let data = await response.json()
	return data
}


export default createDataSet;