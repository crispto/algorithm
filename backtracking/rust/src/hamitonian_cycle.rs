use std::convert::TryFrom;

// rust  从 unsize转成 i32 很麻烦啊
// 二维数组是有语法糖可以直接初始化的；
fn hamitonian_cycle(graph: [[i32; 5]; 5], start: usize) {
    // let path = [0; graph.len()]
    let mut path: [i32; 6] = [-1; 6];
    path[0] = start as i32;
    path[path.len() - 1] = start as i32;
    if hamitonian_cycle_help(&graph, &mut path, 1) {
        println!("{:?}", path);
    } else {
        println!("no cycle")
    }
    return;
}

fn hamitonian_cycle_help(graph: &[[i32; 5]; 5], path: &mut [i32; 6], path_index: usize) -> bool {
    if path_index == graph.len() {
        let last = usize::try_from(path[path_index - 1]).unwrap();
        return graph[last][0] == 1;
    }
    for i in 0..graph.len() {
        let current = usize::try_from(path[path_index - 1]).unwrap();
        if is_valid(graph, current, i, path) {
            path[path_index] = i as i32;
            if hamitonian_cycle_help(graph, path, path_index + 1) {
                return true;
            }
            path[path_index] = -1;
        }
    }
    return false;
}
fn is_valid(graph: &[[i32; 5]; 5], current: usize, next: usize, path: &[i32; 6]) -> bool {
    if graph[current][next] == 0 {
        return false;
    }
    for v in path {
        if *v == next as i32 {
            return false;
        }
    }
    return true;
}

pub fn hamitonian_cycle_test() {
    let graph: [[i32; 5]; 5] = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 4],
        [0, 1, 1, 4, 0],
    ];
    hamitonian_cycle(graph, 0);
}
