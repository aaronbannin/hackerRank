//: Playground - noun: a place where people can play

import Cocoa

//var str = "Hello, playground"


let int = 5

func factorial(N: Int) -> Int {
    if N == 1 {
        return 1
    } else {
        return N * factorial(N - 1)
    }
}

factorial(int)