cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(delaunay C CXX)

set(CMAKE_SKIP_RULE_DEPENDENCY TRUE)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif()

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)

include_directories(${PROJECT_BINARY_DIR})

add_library(
    delaunay
    SHARED
    delaunay.c
    delaunay.h
    )

# we let cmake generate the export header
include(GenerateExportHeader)
generate_export_header(delaunay)
