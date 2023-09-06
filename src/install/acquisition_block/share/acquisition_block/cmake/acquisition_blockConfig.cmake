# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_acquisition_block_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED acquisition_block_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(acquisition_block_FOUND FALSE)
  elseif(NOT acquisition_block_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(acquisition_block_FOUND FALSE)
  endif()
  return()
endif()
set(_acquisition_block_CONFIG_INCLUDED TRUE)

# output package information
if(NOT acquisition_block_FIND_QUIETLY)
  message(STATUS "Found acquisition_block: 0.0.0 (${acquisition_block_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'acquisition_block' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${acquisition_block_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(acquisition_block_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${acquisition_block_DIR}/${_extra}")
endforeach()
