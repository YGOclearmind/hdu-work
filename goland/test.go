package main

import (
    "database/sql"
    "fmt"
    "log"
    "net/http"
    _"github.com/go-sql-driver/mysql"
    "goland/handler"
)

// dbHandler 函数处理数据库请求，查询用户信息并返回
func dbHandler(w http.ResponseWriter, r *http.Request) {
    db, err := sql.Open("mysql", "user:password@tcp(127.0.0.1:3306)/dbname")
    if err != nil {
        log.Fatal(err)
    }
    // 关闭数据库连接，确保在函数执行完毕后资源得到释放
        defer db.Close()

    // 从数据库中查询用户名称的示例代码
    // 该代码查询id为1的用户，并处理可能出现的错误
        var result string
        err = db.QueryRow("SELECT name FROM users WHERE id = 1").Scan(&result)
        if err != nil {
            log.Fatal(err)
        }

    fmt.Fprintf(w, "User name: %s", result)
}

// main 函数启动HTTP服务器并定义路由
func main() {
    http.HandleFunc("/db", handler.HelloHandler)
    fmt.Println("Server is running on http://localhost:8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}