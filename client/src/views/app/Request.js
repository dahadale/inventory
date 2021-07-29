import React, { useState, useEffect, Fragment } from 'react';

const Request = () => {

const [partNumber, setPartNumber] = useState('');
const [dateRequisition, setDateRequisition] = useState('');
const [courseCode, setCourseCode] = useState('');
const [courseNumber, setCourseNumber] = useState('');
const [quantity, setQuantity] = useState('');
const [loading, setLoading] = useState(true);


useEffect(() => {
    if (localStorage.getItem('token') === null) {
        window.location.replace('http://localhost:3000/login');
    } else {
        setLoading(false);
    }
}, []);



const onSubmit = e => {
    e.preventDefault();

    const data = {
        part_number: partNumber,
        dateRequisition: dateRequisition,
        course_code: courseCode,
        courseNumber: courseNumber,
        quantity: quantity
    };
    

    fetch('http://localhost:8000/api/inventory/requisition/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Authorization: `Token ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            
        });

};



  return (
    <div className="container">
        <div className="row d-flex justify-content-center" >
            <div className="col-md-6  d-flex justify-content-center mt-5">
                <div class="card w-75">
                    <div class="card-body">
                        <h5 class="card-title text-center">Request</h5>
                    

                        <form onSubmit={onSubmit}>
                        <div class="row">
                            <div class="col-12">
                                <div class="form-group">
                                    <label for="partNumber">Part Number</label>
                                    <input 
                                    type="text"
                                    className="form-control"
                                    id="partNumber"
                                    aria-describedby="emailHelp"
                                    value={partNumber}
                                    onChange={e => setPartNumber(e.target.value)}
                                    placeholder="Part Number"></input>
                                </div>
                            </div>
                        </div>
                    

                        <div class="row">
                            <div class="col-6">
                                <div class="form-group">
                                    <label for="date">Date</label>
                                    <input
                                    type="date"
                                    className="form-control"
                                    id="date"
                                    value={dateRequisition}
                                    onChange={e => setDateRequisition(e.target.value)}
                                    aria-describedby="emailHelp" placeholder="Course Code"></input>
                                </div>
                            </div>

                            <div class="col-6">

                                <label for="courseCode">Course Code</label>
                                <input
                                type="text"
                                className="form-control"
                                id="courseCode"
                                value={courseCode}
                                onChange={e => setCourseCode(e.target.value)}
                                aria-describedby="emailHelp" placeholder="Course Code"></input>            

                            </div>
                        </div>


                        <div class="row">
                            <div class="col-6">
                                <div class="form-group">
                                    <label for="courseNumber">Course Number</label>
                                    <input
                                    type="text"
                                    className="form-control"
                                    id="courseNumber"
                                    aria-describedby="emailHelp"
                                    value={courseNumber}
                                    onChange={e => setCourseNumber(e.target.value)}
                                    placeholder="Course Number"></input>
                                </div>
                            </div>

                            <div class="col-6">

                                <label for="quantity">Quantity</label>
                                <input
                                type="text"
                                className="form-control"
                                id="quantity"
                                aria-describedby="emailHelp"
                                value={quantity}
                                onChange={e => setQuantity(e.target.value)}
                                placeholder="Quantity"></input>            

                            </div>
                        </div>


                        <div class="row d-flex justify-content-end">
                            <div class="col-6 d-flex justify-content-end">
                                <input type='submit' className="btn btn-primary" value='Submit' />

                            </div>
                        </div>

                        
                    </form>                



                    </div>
                </div>
            </div>



        </div>            
    </div>
  );
};

export default Request;