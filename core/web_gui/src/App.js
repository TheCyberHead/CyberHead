import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Layout, Menu, Icon } from 'antd';

import './App.css';
import Strategies from './components/Strategies';
import Overview from './components/Overview';
import HeatVision from './components/HeatVision';
import DataSets from './components/DataSets';
import Configuration from './components/Configuration';

const { Header, Sider, Content } = Layout;
const { SubMenu } = Menu;

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      collapsed: false,
      selectedKeyMenu: "1"
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
          <img src="images/logo64.png" class="center"/>
          </div>
          <Menu style={{ background: '#141414'}} theme="dark" mode="inline" defaultSelectedKeys={["1"]} selectedKeys={[this.state.selectedKeyMenu]} >
          <Menu.Item className="item"key="1">
                <Link to="/Overview">
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
                <span>Strats</span>
              </span>
            }
          >
            <Menu.Item className="item" key="11">Strategy1</Menu.Item>
            <Menu.Item className="item" key="12">Strategy2</Menu.Item>
            <Menu.Item className="item" key="13">Strategy3</Menu.Item>
          </SubMenu>

            <Menu.Item className="item" key="2">
                <Link to="/strategies">
                  <Icon type="stock" />
                  <span>Strategies</span>
                </Link>



                <Menu.Item className="item" key="21">
                    <Link to="/strategies">
                      <Icon type="stock" />
                      <span>Strategies</span>
                    </Link>
                </Menu.Item>

            </Menu.Item>
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
                <Route path="/strategies">
                  <Strategies updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/heat-vision">
                  <HeatVision updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/datasets">
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
