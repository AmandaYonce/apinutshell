import React, { Component } from 'react'
import { Col, Container, Row, Card, CardText } from "reactstrap";
import { API_SHOE_URL } from "../constants";

class Main extends Component {
  state = {
    shoes: []
  }

  componentDidMount(){
    fetch(API_SHOE_URL).then((res)=>res.json())
    .then((data)=>this.setState({shoes:data}))
  }


  render() {

    return (
        <>
        <h1>Main Page</h1>
        <Container style={{ marginTop: "20px" }}>
          <Row style={{ padding: "60px"}}>
            <Col>
            {this.state.shoes.map(shoe => (
              <Card style={{ marginTop: "20px", padding: "10px", border: "2px solid black", maxWidth: "200px" }}>
                <CardText>Inventory number: {shoe.id}</CardText>
                <CardText>{shoe.brand.brand}</CardText>
                <CardText>{shoe.manufacturer.name}</CardText>
                <CardText>{shoe.shoe_type.style}</CardText>
                <CardText>{shoe.color.color_name}</CardText>
                <CardText>size: {shoe.size.size}</CardText>
                <CardText>{shoe.material.material}</CardText>
                <CardText>{shoe.fastener.fastener}</CardText>
              </Card>

            ))}
            </Col>
          </Row>
        </Container>
        </>
)
}
}

export default Main
