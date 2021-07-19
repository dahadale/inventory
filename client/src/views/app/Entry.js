import React, { useState, useEffect, Fragment } from 'react';

const Entry = () => {

  return (
    <div className="container">
        <div className="row d-flex justify-content-center" >
            <div className="col-md-6  d-flex justify-content-center mt-5">
                <div class="card w-75">
                    <div class="card-body">
                        <h5 class="card-title text-center">Entry</h5>
                    

                        <form>
                        <div class="row">
                            <div class="col-12">
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Part Number</label>
                                    <input type="text" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Part Number"></input>
                                </div>
                            </div>
                        </div>
                    

                        <div class="row">
                            <div class="col-6">
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Date</label>
                                    <input type="date" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Course Code"></input>
                                </div>
                            </div>

                            <div class="col-6">

                                <label for="exampleInputEmail1">Purchase Order</label>
                                <input type="text" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Purchase Order"></input>            

                            </div>
                        </div>


                        <div class="row">
                            <div class="col-6">
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Lot</label>
                                    <input type="text" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Lot"></input>
                                </div>
                            </div>

                            <div class="col-6">

                                <label for="exampleInputEmail1">Owner</label>
                                <input type="text" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Owner"></input>            

                            </div>
                        </div>

                        <div class="row">
                            <div class="col-6">
                                <div class="form-group">
                                    <label for="exampleInputEmail1">Date Shelflife</label>
                                    <input type="date" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Date Shelflife"></input>
                                </div>
                            </div>

                            <div class="col-6">

                                <label for="exampleInputEmail1">Quantity</label>
                                <input type="number" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Quantity"></input>            

                            </div>
                        </div>


                        <div class="row d-flex justify-content-end">
                            <div class="col-6 d-flex justify-content-end">
                                <button type="submit" class="btn btn-primary">Submit</button>
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

export default Entry;