import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Layout, Menu, Icon } from 'antd';

import './App.css';
import Overview from './components/Overview';
import HeatVision from './components/HeatVision';
import DataSets from './components/DataSets';
import Configuration from './components/Configuration';
import Strategy from './components/Strategy';

const { Header, Sider, Content } = Layout;
const { SubMenu } = Menu;

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      collapsed: false,
      selectedKeyMenu: "1",
      strategies: []
    };
    this.updateMenuKey = this.updateMenuKey.bind(this);
  }

  updateMenuKey(key){
    this.setState({selectedKeyMenu: key})
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
          <img src="/images/logo64.png" className="center"/>
          </div>
          <Menu style={{ background: '#141414'}} theme="dark" mode="inline" defaultSelectedKeys={["1"]} selectedKeys={[this.state.selectedKeyMenu]} >
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
            <Menu.Item className="item">
              <Link to="/strategy1">
                <Icon type="stock" />
                <span>CrossGOOG</span>
              </Link>
            </Menu.Item>
            <Menu.Item className="item">
              <Link to="/strategy2">
                <Icon type="stock" />
                <span>CrossGOOG2</span>
              </Link>
              </Menu.Item>
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
              <Switch>
                <Route exact path="/strategy/:strategy_name"  component={Strategy}/>

                <Route exact path="/heat-vision">
                  <HeatVision updateKey={this.updateMenuKey} />
                </Route>

                <Route exact path="/datasets">
                  <DataSets updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/configuration">
                  <Configuration updateKey={this.updateMenuKey} />
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
