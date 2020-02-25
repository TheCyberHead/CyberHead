import React from 'react';
import { Form, Input, Modal, Card, Col, Row, Button, Select } from 'antd';
import getDatasets from '../actions/DataSet';
const { Option } = Select;

class DataSets extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			datasets: [],
			load: true,
			openModal: false
		}
		this.triggerOpenModal = this.triggerOpenModal.bind(this)
		this.submitForm = this.submitForm.bind(this)
	}

	componentDidMount(){
		this.props.updateKey('5')
		getDatasets()
			.then(response => this.setState({datasets: response.datasets}))
	}

	triggerOpenModal(){
		this.setState({openModal: !this.state.openModal})
	}

	submitForm(ev){
		ev.preventDefault()
		const {frecuency, identifier, source, ticker} = this.state
		console.log(frecuency)
	}

	onChangeFields = (e) => {
		this.setState({[e.target.name]: e.target.value});
	}

	setFrecuency = (val) => {
		this.setState({frecuency: val});
	}

	setSource = (val) => {
		this.setState({source: val});
	}

	render(){
		return(
			<React.Fragment>
				<Modal
          title="Add a new data set"
          visible={this.state.openModal}
          onCancel={this.triggerOpenModal}
        >
          <Form layout="horizontal" onSubmit={this.submitForm}>
            <Form.Item>
              <Input placeholder="Identifier. i.e : AMZN 15 min" name="identifier" onChange={this.onChangeFields}/>
            </Form.Item>

            <Form.Item>
              <Input placeholder="Ticker. i.e : MSFT / AMZN" name="ticker" onChange={this.onChangeFields} />
            </Form.Item>

            <Form.Item>
              <Select defaultValue="15m" onChange={this.setFrecuency}>
                    <Option value="1m">1 minute</Option>
                    <Option value="2m">2 minutes</Option>
                    <Option value="5m">5 minutes</Option>
                    <Option value="15m">15 minutes</Option>
                    <Option value="30m">30 minutes</Option>
                    <Option value="60m">60 minutes</Option>
                    <Option value="90m">90 minutes</Option>
                    <Option value="1h">1 hour</Option>
                    <Option value="1d">1 day</Option>
                    <Option value="5d">5 days</Option>
                    <Option value="1wk">1 week</Option>
                    <Option value="1mo">1 month</Option>
                    <Option value="3mo">3 months</Option>
              </Select>
            </Form.Item>

            <Form.Item>
              <Select defaultValue="Yahoo" name="source" onChange={this.setSource}>
                    <Option value="Yahoo">Yahoo</Option>
                    <Option value="Alpaca">Alpaca</Option>
              </Select>
            </Form.Item>


            <Form.Item>
              <Button type="primary" htmlType="submit">Submit</Button>
            </Form.Item>
          </Form>
        </Modal>

				<h1 style={{ color: '#ffffff'}}>Data Sets</h1>
				<div style={{ padding: '30px'}} className="dataset-box">

						<Button type="primary" icon="file-add" size="large" onClick={this.triggerOpenModal} style={{marginRight: '1em'}}>
		          Subscribe from source
		        </Button>

				    <Row gutter={16} style={{marginTop:'1em'}}>
				    {this.state.load && this.state.datasets.map((dataset,index) => (
				    	<Col span={8} key={index}>
				    	  <Card key={index} title={dataset.identifier} bordered={true} className="dataset-card">
				    	    <p>{dataset.description}</p>
				    	    <p><strong>Symbol</strong>: {dataset.reference_symbol}</p>
				    	  </Card>
				    	</Col>
				    ))}
				    </Row>					
				  </div>
			</React.Fragment>
		)
	}
}

export default DataSets;