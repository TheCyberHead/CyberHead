import React from 'react';
import ApexCharts from 'apexcharts'
import {Form,Input, Button} from 'antd';
import submitHeatmap from '../actions/submitHeatmap';

class HeatVision extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true,
			file64: '',
			series: [{
			    name: 'Bubble1',
			    data: [1,1,11,1,1]
			  }],
			  options: {
			    chart: {
			        height: 350,
			        type: 'bubble',
			    },
			    dataLabels: {
			        enabled: false
			    },
			    fill: {
			        opacity: 0.8
			    },
			    title: {
			        text: 'Simple Bubble Chart'
			    },
			    xaxis: {
			        tickAmount: 12,
			        type: 'category',
			    },
			    yaxis: {
			        max: 70
			    }
			  }
		}
	}

	componentDidMount(){
		this.props.updateKey('3')
	}

	fileChange = ev => {
		let reader = new FileReader();
		reader.readAsDataURL(ev.target.files[0])
		reader.onload = () => {
			this.setState({file64: reader.result})
		}
	}

	submitForm = ev => {
		ev.preventDefault()
		const {title, file64} = this.state
		const heatmap = {heatmap: {title, file64}}
		submitHeatmap(heatmap)
			.then(response => console.log(response))
		console.log(file64)
	}

	handleChange = ev => {
		const {name, value} = ev.target
		this.setState({[name]: value})
	}

	render(){
		return(
			<React.Fragment>
				<h1 style={{ color: '#ffffff'}}>Heat Vision</h1>
				<div className="heat-vision">
				<h3>Create a heat map</h3>
				<Form layout="horizontal" className="heatmap-upload-form" onSubmit={this.submitForm}>
					<Form.Item>
						<Input placeholder="Heat Map Identificator" name="title" onChange={this.handleChange}/>
					</Form.Item>

					<Form.Item>
						<input type="file" onChange={this.fileChange} className="heat-upload-file"/>
					</Form.Item>


					<Form.Item>
					  <Button type="primary" htmlType="submit">Upload</Button>
					</Form.Item>
				</Form>
				<div className="heatmap-list">
					<ul>
						<li>
							<p>Heatmap 1</p>
						</li>
						<li>
							<p>Heatmap 2</p>
						</li>
						<li>
							<p>Heatmap 3</p>
						</li>
						<li>
							<p>Heatmap 4</p>
						</li>
						<li>
							<p>Heatmap 5</p>
						</li>
						<li>
							<p>Heatmap 6</p>
						</li>
					</ul>
				</div>
				</div>
				
			</React.Fragment>
		)
	}
}

export default HeatVision;