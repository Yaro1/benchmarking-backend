package main

import (
    "net/http"
    "github.com/labstack/echo/v4"
    "app/functions"
)

func main() {
    e := echo.New()

    
    e.POST("/compute", func(c echo.Context) error {
        nums, err := functions.DecodeRequest(c.Request())
        if err != nil {
            return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
        }
        return c.JSON(http.StatusOK, map[string]interface{}{ "result": functions.Compute(nums.Numbers) })
    })
    
    e.POST("/multiply", func(c echo.Context) error {
        nums, err := functions.DecodeRequest(c.Request())
        if err != nil {
            return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
        }
        return c.JSON(http.StatusOK, map[string]interface{}{ "result": functions.Multiply(nums.Numbers) })
    })
    
    e.POST("/average", func(c echo.Context) error {
        nums, err := functions.DecodeRequest(c.Request())
        if err != nil {
            return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
        }
        return c.JSON(http.StatusOK, map[string]interface{}{ "result": functions.Average(nums.Numbers) })
    })
    

    e.Start(":8000")
}