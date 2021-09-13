" Vim setting based on Vundle
" git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
" or simply use https://github.com/amix/vimrc
" Launch vim and run :PluginInstall
" To install from command line: vim +PluginInstall +qall
set nocompatible
filetype off
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
set cursorline
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-surround'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/nerdtree'
Plugin 'altercation/vim-colors-solarized'
Plugin 'ervandew/supertab'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" nerdtree settings
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" vim-colors-solarized settings
set t_Co=256 " to support tmux env
let g:solarized_termcolors=256
syntax enable
set background=dark
colorscheme solarized
