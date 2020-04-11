import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { Layout, Menu, Icon } from 'antd';
import Overview from './components/Overview';
import HeatVision from './components/HeatVision';
import DataSets from './components/DataSets';
import Configuration from './components/Configuration';
import Strategy from './components/Strategy';
import Brokers from './components/Brokers';
import CodeEditor from './components/CodeEditor';
import {getStrategies} from './actions/strategies'
import './App.css';


// Automated Import //


// Automated Import //


const { Header, Sider, Content } = Layout;
const { SubMenu } = Menu;

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      collapsed: false,
      selectedKeyMenu: "1",
      loaded: false,
      strategies: []
    };
    this.updateMenuKey = this.updateMenuKey.bind(this);
    this.loadStrategies = this.loadStrategies.bind(this);
  }

  updateMenuKey(key){
    this.setState({selectedKeyMenu: key})
  }

  loadStrategies(){
    getStrategies()
      .then(response => {
        response.strategies.map(strategy => this.setState({strategies: [...this.state.strategies, strategy.strategy_name]}))
      })
  }

  componentDidMount(){
    this.loadStrategies()
    this.setState({loaded: true})
  }

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  };

  render() {
    return (
      <Router>
      <Layout>
        <Sider trigger={null} collapsible collapsed={this.state.collapsed} style={{ background: '#141414'}}>
          <div className="logo">
          <img src="/images/logo64.png" className="center" alt="logo"/>
          </div>
          <Menu style={{ background: '#141414'}} theme="dark" mode="inline" defaultSelectedKeys={["1"]} selectedKeys={[this.state.selectedKeyMenu]} >


{/* Automated Menu */}


{/* Automated Menu */}
	    
	    
          <Menu.Item className="item"key="1">
                <Link to="/overview">
            <Icon type="desktop" />
            <span>Porfolio</span>

                </Link>
          </Menu.Item>
          <SubMenu
            style={{ background: '#141414'}}
            theme="dark"
            mode="inline"
            key="sub1"
            title={
              <span>
                <Icon type="stock" />
                <span>Strategies</span>
              </span>
            }
          >
            {this.state.loaded && this.state.strategies.map((strategy, index) => (
              <Menu.Item className="item" key={index+11}>
                <Link to={`/strategy/${strategy}`}>
                  <Icon type="stock" />
                  <span>{strategy}</span>
                </Link>
              </Menu.Item>
            ))}
          </SubMenu>

            <Menu.Item className="item" key="3">
              <Link to="/heat-vision">
                <Icon type="dot-chart" />
                <span>Heat Vision</span>
              </Link>
            </Menu.Item>

            <Menu.Item className="item" key="4">
              <Link  to="configuration">
                <Icon type="experiment" />
                <span>Configuration</span>
              </Link>
            </Menu.Item>

            <Menu.Item className="item" key="5">
              <Link to="/datasets">
                <Icon type="file-add" />
                <span>Data Sets</span>
              </Link>
            </Menu.Item>

            <Menu.Item className="item" key="6">
              <Link to="/brokers">
                <Icon type="sliders" />
                <span>Broker Accounts</span>
              </Link>
            </Menu.Item>

            <Menu.Item className="item" key="7">
              <Link to="/editor">
                <Icon type="sliders" />
                <span>Editor</span>
              </Link>
            </Menu.Item>

          </Menu>
        </Sider>

        <Layout>
          <Header style={{ background: '#090909'}}>
            <Icon
              className="trigger"
              type={this.state.collapsed ? 'menu-unfold' : 'menu-fold'}
              onClick={this.toggle}
            />
          </Header>
          <Content
            style={{
              margin: '0px 0px',
              padding: 24,
              background: '#1b1b1b',
              minHeight: '100vh',
            }}
          >


            </Switch>


{/* Automated Route */}


{/* Automated Route */}


                <Route exact path="/datasets">
                  <DataSets updateKey={this.updateMenuKey} />
                </Route>

                <Route exact path="/configuration">
                  <Configuration updateKey={this.updateMenuKey} />
                </Route>

                <Route exact path="/brokers">
                  <Brokers updateKey={this.updateMenuKey} />
                </Route>

                <Route exact path="/editor">
                  <CodeEditor updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/">
                  <Overview updateKey={this.updateMenuKey} />
                </Route>
              </Switch>

          </Content>
        </Layout>
      </Layout>
      </Router>
    );
  }
}

export default App;
