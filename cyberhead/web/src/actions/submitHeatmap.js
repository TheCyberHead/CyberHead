import API_BASE from './URL'

async function submitHeatmap(heatmap){
	let response = await fetch(`${API_BASE}/heatmap`,{
			method: 'POST',
			body: JSON.stringify(heatmap),
			headers:{
				'Content-Type': 'application/json'
			}
		})
	let data = await response.json()
	return data
}


export default submitHeatmap;