package main

import (
    "net/http"
    "encoding/json"
    "app/functions"
)

type Response struct {
    Result interface{} `json:"result"`
}


func ComputeHandler(w http.ResponseWriter, r *http.Request) {
    items, err := functions.DecodeRequest(r)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    json.NewEncoder(w).Encode(Response{Result: functions.Compute(items.Items)})
}

func MultiplyHandler(w http.ResponseWriter, r *http.Request) {
    items, err := functions.DecodeRequest(r)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    json.NewEncoder(w).Encode(Response{Result: functions.Multiply(items.Items)})
}

func AverageHandler(w http.ResponseWriter, r *http.Request) {
    items, err := functions.DecodeRequest(r)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    json.NewEncoder(w).Encode(Response{Result: functions.Average(items.Items)})
}


func main() {
    
    http.HandleFunc("/compute", ComputeHandler)
    
    http.HandleFunc("/multiply", MultiplyHandler)
    
    http.HandleFunc("/average", AverageHandler)
    

    http.ListenAndServe(":8000", nil)
}