cmake_minimum_required(VERSION 3.15)
project(mapviewer VERSION 1.0 LANGUAGES CXX)

find_package(graphics CONFIG REQUIRED)
add_executable(mapviewer src/mapviewer.cpp src/main.cpp)
target_compile_definitions(mapviewer PRIVATE PKG_VERSION="${PROJECT_VERSION}")
target_link_libraries(mapviewer graphics::graphics)

install(TARGETS mapviewer DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
)
