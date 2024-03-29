use std::io::stdin;
use std::str::FromStr;

fn input_t<T: FromStr>() -> T {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    s.trim().parse().ok().unwrap()
}

fn div_list(x: usize) -> Vec<usize> {
    let mut div_l: Vec<usize> = Vec::new();
    let mut div_r: Vec<usize> = Vec::new();
    let mut i: usize = 1;
    while i * i <= x {
        if x % i == 0 {
            div_l.push(i);
            if i != x / i {
                div_r.push(x / i);
            }
        }
        i += 1;
    }
    div_l.iter().cloned().chain(div_r.iter().rev().cloned()).collect()
}

fn main() {
    let n: usize = input_t();
    for x in div_list(n) {
        println!("{}", x);
    }
}
