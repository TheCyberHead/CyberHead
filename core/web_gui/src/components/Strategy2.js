import React from 'react';
import { Card, Col, Row } from 'antd';

class Strategies extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('12')
	}

	render(){
		return(
			<React.Fragment>
				<h1 style={{ color: '#ffffff'}}>Strategy 2</h1>
				<hr/>
				<div style={{ padding: '30px' }}>
				    <Row gutter={16}>
				      <Col span={8}>
				        <Card title="Strategy Indicator 1" bordered={false}>
				          Value 1
				        </Card>
				      </Col>
				      <Col span={8}>
				        <Card title="Strategy Indicator 2" bordered={false}>
				          Value 2
				        </Card>
				      </Col>
				      <Col span={8}>
				        <Card title="Strategy Indicator 3" bordered={false}>
				          Value 3
				        </Card>
				      </Col>
				    </Row>
				  </div>
				<iframe src="https://cyberhead.s3.amazonaws.com/SmaCross.html" width="100%" height="800"></iframe>
			</React.Fragment>
		)
	}
}

export default Strategies;
