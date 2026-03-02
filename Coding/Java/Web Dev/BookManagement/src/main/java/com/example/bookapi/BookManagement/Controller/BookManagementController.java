package com.example.bookapi.BookManagement.Controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/bookApi/books")
class BookManagementController {
    @GetMapping("/")
    void getAllBooks(){

    }

    @GetMapping("/{@requestedId}")
    void getBookById(@PathVariable Long requestedId){

    }
}
