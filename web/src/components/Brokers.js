import React from 'react';
import alpaca from '../alpaca.png'
import ameritrade from '../ameritrade.svg'
import coinbase from '../coinbase.svg'
import {Form,Input,Button,Select} from 'antd';

const { Option } = Select;


class Brokers extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('6')
	}

	render(){
		return(
			<div className="brokers_section">
				<div className="submit-broker">
					<div className="account_form">
						<Form layout="horizontal">
						  <Form.Item>
						    <Select defaultValue="Alpaca" >
	                 <Option value="Alpaca">Alpaca</Option>
	                 <Option value="Ameritrade">TD Ameritrade</Option>
	                 <Option value="Coinbase">Coinbase</Option>
	               </Select>
						  </Form.Item>
						  <Form.Item>
						    <Input placeholder="API Key" />
						  </Form.Item>

						  <Form.Item>
						    <Input placeholder="API Secret" />
						  </Form.Item>

						  <Form.Item>
						    <Input placeholder="API Passphrase" />
						  </Form.Item>

						  <Form.Item>
						    <Button type="primary">Submit account</Button>
						  </Form.Item>
						</Form>
					</div>

					<h3>Supported Brokers</h3>
					<div className="logo-box">
						<img src={alpaca}/>
						<img src={ameritrade}/>
						<img src={coinbase}/>
					</div>
				</div>
				<div className="broker_accounts">
					<h1>Broker Accounts</h1>
					<p>
						Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium.
							
						Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc.
							
						Quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing.
					</p>
				</div>
			</div>
		)
	}
}

export default Brokers;