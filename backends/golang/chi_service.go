package main

import (
    "encoding/json"
    "net/http"
    "app/functions"
    "github.com/go-chi/chi/v5"
)


func ComputeHandler(w http.ResponseWriter, r *http.Request) {
    items, err := functions.DecodeRequest(r)
    w.Header().Set("Content-Type", "application/json")

    if err != nil {
        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(map[string]string{"error": err.Error()})
        return
    }

    json.NewEncoder(w).Encode(map[string]interface{}{"result": functions.Compute(items.Items)})
}

func MultiplyHandler(w http.ResponseWriter, r *http.Request) {
    items, err := functions.DecodeRequest(r)
    w.Header().Set("Content-Type", "application/json")

    if err != nil {
        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(map[string]string{"error": err.Error()})
        return
    }

    json.NewEncoder(w).Encode(map[string]interface{}{"result": functions.Multiply(items.Items)})
}

func AverageHandler(w http.ResponseWriter, r *http.Request) {
    items, err := functions.DecodeRequest(r)
    w.Header().Set("Content-Type", "application/json")

    if err != nil {
        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(map[string]string{"error": err.Error()})
        return
    }

    json.NewEncoder(w).Encode(map[string]interface{}{"result": functions.Average(items.Items)})
}


func main() {
    r := chi.NewRouter()

    
    r.Post("/compute", ComputeHandler)
    
    r.Post("/multiply", MultiplyHandler)
    
    r.Post("/average", AverageHandler)
    

    http.ListenAndServe(":8000", r)
}