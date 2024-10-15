package handler
import (
    "fmt"
    "net/http"
)

// helloHandler 处理根路径的请求，并返回欢迎信息
func HelloHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, `pjsb！`)
}
