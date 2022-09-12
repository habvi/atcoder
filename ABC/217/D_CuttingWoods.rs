use std::io::stdin;
use std::str::FromStr;
use std::collections::BTreeSet;

fn input_tuple<T: FromStr>() -> (T, T) {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    let mut itr = s.split_whitespace();
    (
        itr.next().unwrap().parse().ok().unwrap(),
        itr.next().unwrap().parse().ok().unwrap()
    )
}

fn main() {
    let (l, q): (usize, usize) = input_tuple();
    let mut s = BTreeSet::new();
    s.insert(0);
    s.insert(l);
    for _ in 0..q {
        let (c, x): (usize, usize) = input_tuple();
        match c {
            1 => {
                s.insert(x);
            },
            2 => {
                let left = *s.range(..x).next_back().unwrap();
                let right = *s.range(x..).next().unwrap();
                println!("{}", right - left);
            },
            _ => unreachable!(),
        }
    }
}
