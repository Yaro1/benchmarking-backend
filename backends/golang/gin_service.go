package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
    "app/functions"
)

func main() {
    r := gin.Default()

    
    r.POST("/compute", func(c *gin.Context) {
        items, err := functions.DecodeRequest(c.Request)
        if err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }
        c.JSON(http.StatusOK, gin.H{"result": functions.Compute(items.Items)})
    })
    
    r.POST("/multiply", func(c *gin.Context) {
        items, err := functions.DecodeRequest(c.Request)
        if err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }
        c.JSON(http.StatusOK, gin.H{"result": functions.Multiply(items.Items)})
    })
    
    r.POST("/average", func(c *gin.Context) {
        items, err := functions.DecodeRequest(c.Request)
        if err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }
        c.JSON(http.StatusOK, gin.H{"result": functions.Average(items.Items)})
    })
    

    r.Run(":8000")
}