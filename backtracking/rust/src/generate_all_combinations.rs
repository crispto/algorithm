pub fn all_combitions(n: usize, k: usize) {
    let q = generate_all_combinations(4, 2);
    for element in q.iter() {
        println!("{:?}", element);
    }
}

//generate_all_combinations 产生所有的组合
fn generate_all_combinations(n: usize, k: usize) -> Vec<Vec<usize>> {
    if n < k {
        panic!("无效参数")
    }

    let mut result: Vec<Vec<usize>> = Vec::new();
    let mut tmp: Vec<usize> = Vec::new();
    generate_all_combinations_help(1, n, k, &mut tmp, &mut result);
    return result;
}

fn generate_all_combinations_help(
    start: usize,
    n: usize,
    k: usize,
    tmp: &mut Vec<usize>,
    result: &mut Vec<Vec<usize>>,
) {
    if tmp.len() == k {
        result.push(tmp.clone());
        return;
    }
    let end = n - k + 2;
    for i in start..end {
        tmp.push(i);
        generate_all_combinations_help(start + 1, n, k, tmp, result);
        tmp.pop();
    }
}
